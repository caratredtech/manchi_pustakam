import json
import frappe

def update_workspace():
    # Read the workspace JSON file
    with open('/home/caratred/frappev16/apps/manchipustakam/manchipustakam/manchi_pustakam/workspace/manchi_pustakam/manchi_pustakam.json', 'r') as f:
        data = json.load(f)

    # Get the workspace doc
    workspace = frappe.get_doc('Workspace', 'Manchi Pustakam')
    workspace.content = data.get('content', '[]')
    workspace.save()
    frappe.db.commit()

    print('Workspace updated successfully')
    print('Content length:', len(workspace.content))

if __name__ == '__main__':
    import os
    os.chdir('/home/caratred/frappev16')
    frappe.init('frappemanchi.local')
    frappe.connect()
    update_workspace()
