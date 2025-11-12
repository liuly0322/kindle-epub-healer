#!/usr/bin/env python3
"""
EPUB Healer - Fixes EPUB files to be compatible with Kindle's kindlegen tool
"""

import os
import sys
import zipfile
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict


class EPUBHealer:
    def __init__(self, epub_path):
        self.epub_path = Path(epub_path)
        self.work_dir = Path('/tmp/epub_healer_work')
        self.extract_dir = self.work_dir / 'extracted'
        
    def extract_epub(self):
        """Extract EPUB file to working directory"""
        if self.work_dir.exists():
            shutil.rmtree(self.work_dir)
        self.work_dir.mkdir(parents=True)
        self.extract_dir.mkdir(parents=True)
        
        print(f"Extracting EPUB: {self.epub_path}")
        with zipfile.ZipFile(self.epub_path, 'r') as zip_ref:
            zip_ref.extractall(self.extract_dir)
        print("Extraction complete")
        
    def find_content_opf(self):
        """Find the content.opf file in the EPUB structure"""
        # Common locations
        possible_paths = [
            self.extract_dir / 'OEBPS' / 'content.opf',
            self.extract_dir / 'EPUB' / 'content.opf',
            self.extract_dir / 'content.opf',
        ]
        
        for path in possible_paths:
            if path.exists():
                return path
                
        # Search recursively if not in common locations
        for path in self.extract_dir.rglob('content.opf'):
            return path
            
        raise FileNotFoundError("content.opf not found in EPUB")
        
    def fix_content_opf(self, opf_path):
        """Fix duplicate entries in content.opf manifest"""
        print(f"Analyzing: {opf_path}")
        
        # Register namespaces to preserve them
        namespaces = {
            'opf': 'http://www.idpf.org/2007/opf',
            'dc': 'http://purl.org/dc/elements/1.1/'
        }
        
        for prefix, uri in namespaces.items():
            ET.register_namespace(prefix, uri)
        ET.register_namespace('', 'http://www.idpf.org/2007/opf')
        
        # Parse the OPF file
        tree = ET.parse(opf_path)
        root = tree.getroot()
        
        # Find manifest element
        manifest = root.find('.//{http://www.idpf.org/2007/opf}manifest')
        if manifest is None:
            print("Warning: No manifest found")
            return False
            
        # Track seen IDs and HREFs
        seen_ids = {}
        duplicates_found = False
        items_to_remove = []
        
        for item in manifest.findall('{http://www.idpf.org/2007/opf}item'):
            item_id = item.get('id')
            item_href = item.get('href')
            
            if item_id in seen_ids:
                print(f"  Found duplicate ID: {item_id} (href: {item_href})")
                duplicates_found = True
                # Mark for removal (keep the first occurrence)
                items_to_remove.append(item)
            else:
                seen_ids[item_id] = item_href
                
        # Remove duplicate items
        for item in items_to_remove:
            manifest.remove(item)
            print(f"  Removed duplicate: {item.get('id')}")
            
        if duplicates_found:
            # Write back the fixed content.opf
            tree.write(opf_path, encoding='utf-8', xml_declaration=True)
            print("Fixed content.opf - duplicates removed")
            return True
        else:
            print("No duplicates found in content.opf")
            return False
            
    def repackage_epub(self, output_path):
        """Repackage the fixed EPUB"""
        print(f"Creating fixed EPUB: {output_path}")
        
        # EPUB files must have mimetype as first file, uncompressed
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add mimetype first, uncompressed
            mimetype_path = self.extract_dir / 'mimetype'
            if mimetype_path.exists():
                zipf.write(mimetype_path, 'mimetype', compress_type=zipfile.ZIP_STORED)
            
            # Add all other files
            for file_path in self.extract_dir.rglob('*'):
                if file_path.is_file() and file_path.name != 'mimetype':
                    arcname = file_path.relative_to(self.extract_dir)
                    zipf.write(file_path, arcname, compress_type=zipfile.ZIP_DEFLATED)
                    
        print("EPUB repackaged successfully")
        
    def heal(self):
        """Main healing process"""
        print(f"\n{'='*60}")
        print("Starting EPUB Healer")
        print(f"{'='*60}\n")
        
        try:
            # Extract EPUB
            self.extract_epub()
            
            # Find and fix content.opf
            opf_path = self.find_content_opf()
            self.fix_content_opf(opf_path)
            
            # Create output filename
            output_filename = f"fixed_{self.epub_path.name}"
            output_path = self.epub_path.parent / output_filename
            
            # Repackage EPUB
            self.repackage_epub(output_path)
            
            print(f"\n{'='*60}")
            print(f"Success! Fixed EPUB saved as: {output_filename}")
            print(f"{'='*60}\n")
            
            return output_path
            
        except Exception as e:
            print(f"\nError during healing: {e}")
            import traceback
            traceback.print_exc()
            return None
        finally:
            # Cleanup
            if self.work_dir.exists():
                shutil.rmtree(self.work_dir)


def main():
    if len(sys.argv) < 2:
        print("Usage: python epub_healer.py <epub_file>")
        sys.exit(1)
        
    epub_file = sys.argv[1]
    if not os.path.exists(epub_file):
        print(f"Error: File not found: {epub_file}")
        sys.exit(1)
        
    healer = EPUBHealer(epub_file)
    result = healer.heal()
    
    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
