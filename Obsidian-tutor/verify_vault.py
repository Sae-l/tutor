"""Lesende Vault-Prüfung mit der Python-Standardbibliothek."""
import hashlib
import json
import re
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def targets(text):
    text = re.sub(r"^```.*?^```[^\n]*", "", text, flags=re.M | re.S)
    return [link.split("|", 1)[0] for link in re.findall(r"!?\[\[([^\]]+)\]\]", text)]


def resolve(target, files, current):
    name, _, anchor = target.partition("#")
    path = current if not name else files.get(name)
    if path is None:
        raise ValueError(f"Fehlendes Linkziel: {target}")
    if anchor:
        headings = re.findall(r"^#{1,6}\s+(.+?)\s*$", path.read_text(encoding="utf-8"), re.M)
        if anchor not in headings:
            raise ValueError(f"Fehlende Überschrift: {target}")
    return path


def self_check():
    if targets('[[one|label]] ![[two]]\n```text\n[[ignored]]\n```') != ['one', 'two']:
        raise AssertionError('Wikilink-Selbstprüfung fehlgeschlagen')
    for target in ('missing', '#missing'):
        try:
            resolve(target, {}, Path(__file__))
        except ValueError:
            pass
        else:
            raise AssertionError('Defekte Referenz wurde akzeptiert')


def main():
    self_check()
    if (ROOT / '.obsidian').exists():
        raise ValueError('Persönliche Obsidian-Konfiguration im öffentlichen Vault')
    files = {}
    for path in ROOT.iterdir():
        if path.is_file():
            if path.suffix in {'.md', '.json', '.canvas'}:
                text = path.read_text(encoding='utf-8')
                if re.search(r'(?<![A-Za-z])(?:[A-Za-z]:[\\/]|file://|https://chatgpt\.com/s/)', text):
                    raise ValueError(f'Gerätepfad oder privater Gesprächslink: {path.name}')
            files[path.name] = path
            if path.suffix == '.md':
                files[path.stem] = path
    notes = sorted(ROOT.glob('*.md'))
    graph = {}
    count = 0
    for path in notes:
        text = path.read_text(encoding='utf-8')
        if not text.startswith('---\n') or '\n---\n' not in text[4:]:
            raise ValueError(f'Fehlende Properties: {path.name}')
        frontmatter = text.split('---', 2)[1]
        for field in ('title', 'tags', 'updated'):
            if not re.search(rf'^{field}:', frontmatter, re.M):
                raise ValueError(f'Fehlendes Feld {field}: {path.name}')
        if len(re.findall(r'^```', text, re.M)) % 2:
            raise ValueError(f'Offener Codeblock: {path.name}')
        links = targets(text)
        graph[path] = {resolve(link, files, path) for link in links}
        count += len(links)
    home = files['00 Startseite']
    seen, queue = set(), deque([home])
    while queue:
        path = queue.popleft()
        if path not in seen:
            seen.add(path)
            queue.extend(graph.get(path, set()))
    if set(notes) - seen:
        raise ValueError('Nicht erreichbare Notizen')
    canvas = json.loads((ROOT / 'Tutor-Landkarte.canvas').read_text(encoding='utf-8'))
    ids = [node['id'] for node in canvas['nodes']]
    edge_ids = [edge['id'] for edge in canvas['edges']]
    if len(set(ids + edge_ids)) != len(ids + edge_ids):
        raise ValueError('Doppelte Canvas-Kennung')
    for node in canvas['nodes']:
        if node['type'] == 'file':
            file = (ROOT / node['file']).resolve()
            if not file.is_relative_to(ROOT) or not file.is_file():
                raise ValueError(f'Ungültige Canvas-Datei: {node["file"]}')
        if node['width'] <= 0 or node['height'] <= 0:
            raise ValueError('Ungültige Canvas-Größe')
    cards = [node['file'] for node in canvas['nodes'] if node['type'] == 'file']
    if sorted(cards) != sorted(path.name for path in notes):
        raise ValueError('Canvas muss jede Fachnotiz genau einmal enthalten')
    for edge in canvas['edges']:
        if edge['fromNode'] not in ids or edge['toNode'] not in ids:
            raise ValueError('Canvas-Kante ohne gültiges Ziel')
    manifest = json.loads((ROOT / 'Quellen.sha256.json').read_text(encoding='utf-8'))
    repo = ROOT.parent
    for entry in manifest['files']:
        source = (repo / entry['path']).resolve()
        if not source.is_relative_to(repo) or not source.is_file():
            raise ValueError(f'Ungültige Quelle: {entry["path"]}')
        data = source.read_bytes()
        if entry.get('normalization') == 'utf8-lf':
            data = data.decode('utf-8').replace('\r\n', '\n').encode('utf-8')
        if hashlib.sha256(data).hexdigest() != entry['sha256']:
            raise ValueError(f'Quelle verändert: {entry["path"]}')
    modes = sorted((repo / 'tutor/modes').glob('*.md'))
    mode_note = files['06 Modi'].read_text(encoding='utf-8')
    if len(modes) != 11 or any(f'`{path.name}`' not in mode_note for path in modes):
        raise ValueError('Modusübersicht weicht von der Quelle ab')
    print(json.dumps({'status': 'PASS', 'notes': len(notes), 'wikilinks': count,
                      'canvas_nodes': len(ids), 'canvas_edges': len(edge_ids),
                      'canvas_file_cards': len(cards), 'all_notes_on_canvas': True,
                      'source_hashes': len(manifest['files']), 'modes': len(modes),
                      'negative_self_checks': 2,
                      'limits': ['Keine native Obsidian-Darstellungsprüfung', 'Keine Modell- oder Plattformabnahme']},
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
