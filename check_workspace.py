#!/usr/bin/env python3
import frappe

def check_workspace():
    frappe.init(site='frappemanchi.local')
    frappe.connect()

    try:
        ws = frappe.get_doc('Workspace', 'Manchi Pustakam')
        print(f"✅ Workspace found in database!")
        print(f"   Name: {ws.name}")
        print(f"   Label: {ws.label}")
        print(f"   Module: {ws.module}")
        print(f"   Public: {ws.public}")
        print(f"   Is Standard: {ws.is_standard}")
        print(f"   Icon: {ws.icon}")
        print(f"   Content length: {len(ws.content) if ws.content else 0} chars")

        # Check if content is valid
        import json
        if ws.content:
            content = json.loads(ws.content)
            print(f"   Content items: {len(content)}")

        return True
    except frappe.DoesNotExistError:
        print("❌ Workspace 'Manchi Pustakam' not found in database")
        return False
    except Exception as e:
        print(f"❌ Error checking workspace: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        frappe.destroy()

if __name__ == "__main__":
    check_workspace()
