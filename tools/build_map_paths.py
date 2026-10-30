"""Convert published Bangladesh ADM2 GeoJSON to browser-independent SVG paths."""
from __future__ import annotations

import json
from pathlib import Path

SOURCE = Path('dashboard/data/bangladesh-districts.geojson')
TARGET = Path('dashboard/data/bangladesh-district-paths.json')
ALIASES = {
    'Barisal': 'Barishal', 'Bogra': 'Bogura', 'Brahamanbaria': 'Brahmanbaria',
    'Chittagong': 'Chattogram', "Cox's Bazar": 'Coxsbazar', 'Jessore': 'Jashore',
    'Jhalokati': 'Jhalokathi', 'Maulvibazar': 'Moulvibazar',
    'Nawabganj': 'Chapainawabganj', 'Netrakona': 'Netrokona',
}

def rings(geometry):
    if geometry['type'] == 'Polygon':
        return geometry['coordinates']
    return [ring for polygon in geometry['coordinates'] for ring in polygon]

def main():
    source = json.loads(SOURCE.read_text(encoding='utf-8'))
    points = [point for feature in source['features'] for ring in rings(feature['geometry']) for point in ring]
    min_lon, max_lon = min(p[0] for p in points), max(p[0] for p in points)
    min_lat, max_lat = min(p[1] for p in points), max(p[1] for p in points)
    scale = min(500 / (max_lon - min_lon), 540 / (max_lat - min_lat))
    offset_x = (600 - (max_lon - min_lon) * scale) / 2
    offset_y = 30
    def project(point):
        return offset_x + (point[0] - min_lon) * scale, offset_y + (max_lat - point[1]) * scale
    paths = []
    for feature in source['features']:
        sections=[]
        for ring in rings(feature['geometry']):
            coords=[project(p) for p in ring]
            if not coords: continue
            sections.append('M' + 'L'.join(f'{x:.2f},{y:.2f}' for x,y in coords) + 'Z')
        name=feature['properties']['shapeName']
        paths.append({'district': ALIASES.get(name,name), 'path': ''.join(sections)})
    TARGET.write_text(json.dumps({'source':'geoBoundaries BGD ADM2 2020, BBS/OCHA ROAP','paths':paths},separators=(',',':')),encoding='utf-8')
    print(f'Wrote {len(paths)} district paths to {TARGET}')

if __name__ == '__main__': main()
