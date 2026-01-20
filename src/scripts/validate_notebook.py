import json
import ast
import sys

def validate_notebook(notebook_path):
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except Exception as e:
        print(f"Error loading notebook: {e}")
        return

    code_cell_index = 0
    errors_found = False

    for i, cell in enumerate(nb.get('cells', [])):
        if cell.get('cell_type') == 'code':
            code_cell_index += 1
            source = "".join(cell.get('source', []))
            
            # Skip empty cells or magic commands checks strictly for this validation
            # We want to catch the "invalid decimal literal"
            # However, magic commands starting with % might confuse ast.parse if not handled.
            # But the error reported is "invalid decimal literal", which usually implies something like 1.2.3 or 1e
            
            # Simple cleaning for magic commands for validation purposes
            clean_source_lines = []
            for line in source.splitlines():
                if line.strip().startswith('%') or line.strip().startswith('!'):
                    clean_source_lines.append("pass") # Replace magic with pass to keep line numbers
                else:
                    clean_source_lines.append(line)
            
            clean_source = "\n".join(clean_source_lines)

            try:
                ast.parse(clean_source)
            except SyntaxError as e:
                errors_found = True
                print(f"Syntax Error in Cell Index {i} (Code Cell {code_cell_index}):")
                print(f"  Line {e.lineno}: {e.text.strip() if e.text else 'Unknown'}")
                print(f"  Error: {e.msg}")
                print("-" * 30)

    if not errors_found:
        print("No syntax errors found in code cells.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_notebook.py <notebook_path>")
    else:
        validate_notebook(sys.argv[1])
