#!/usr/bin/env python3
"""
Luke Hydro CRM Backend Server
Simple Flask API for reading/writing to CSV
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

CSV_FILE = 'LukeHydroCRM.csv'
CSV_HEADERS = ['Date Contacted', 'PIC', 'Business', 'Number', 'Location',
               'Attempts', 'Notes', 'Probability', 'Email', 'Business Type', 'Starred']


def read_contacts():
    """Read all contacts from CSV"""
    contacts = []

    if not os.path.exists(CSV_FILE):
        # Create empty CSV with headers if it doesn't exist
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)
        return contacts

    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert 'Starred' string to boolean
            row['starred'] = row.get('Starred', 'false').lower() == 'true'
            contacts.append(row)

    return contacts


def write_contacts(contacts):
    """Write all contacts to CSV"""
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
        writer.writeheader()

        for contact in contacts:
            # Convert boolean starred to string
            row = {
                'Date Contacted': contact.get('date', ''),
                'PIC': contact.get('pic', ''),
                'Business': contact.get('business', ''),
                'Number': contact.get('number', ''),
                'Location': contact.get('location', ''),
                'Attempts': contact.get('attempts', '0'),
                'Notes': contact.get('notes', ''),
                'Probability': contact.get('probability', ''),
                'Email': contact.get('email', ''),
                'Business Type': contact.get('businessType', ''),
                'Starred': str(contact.get('starred', False)).lower()
            }
            writer.writerow(row)


@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    """Get all contacts"""
    try:
        contacts = read_contacts()
        return jsonify({'success': True, 'contacts': contacts})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/contacts', methods=['POST'])
def add_contact():
    """Add a new contact"""
    try:
        new_contact = request.json
        contacts = read_contacts()
        contacts.append(new_contact)
        write_contacts(contacts)

        return jsonify({'success': True, 'message': 'Contact added successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/contacts/<int:index>', methods=['PUT'])
def update_contact(index):
    """Update a contact by index"""
    try:
        updated_contact = request.json
        contacts = read_contacts()

        if index < 0 or index >= len(contacts):
            return jsonify({'success': False, 'error': 'Contact not found'}), 404

        contacts[index] = updated_contact
        write_contacts(contacts)

        return jsonify({'success': True, 'message': 'Contact updated successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/contacts/<int:index>', methods=['DELETE'])
def delete_contact(index):
    """Delete a contact by index"""
    try:
        contacts = read_contacts()

        if index < 0 or index >= len(contacts):
            return jsonify({'success': False, 'error': 'Contact not found'}), 404

        contacts.pop(index)
        write_contacts(contacts)

        return jsonify({'success': True, 'message': 'Contact deleted successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/contacts/bulk', methods=['POST'])
def bulk_update():
    """Update all contacts at once"""
    try:
        all_contacts = request.json.get('contacts', [])
        write_contacts(all_contacts)

        return jsonify({'success': True, 'message': 'All contacts updated successfully'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'csv_file': CSV_FILE,
        'csv_exists': os.path.exists(CSV_FILE)
    })


if __name__ == '__main__':
    print("🚀 Luke Hydro CRM Backend Server")
    print("📊 CSV File:", CSV_FILE)
    print("🌐 Starting server on http://localhost:5000")
    print("🔗 API Endpoints:")
    print("   GET    /api/contacts       - Get all contacts")
    print("   POST   /api/contacts       - Add new contact")
    print("   PUT    /api/contacts/:id   - Update contact")
    print("   DELETE /api/contacts/:id   - Delete contact")
    print("   POST   /api/contacts/bulk  - Bulk update all contacts")
    print("   GET    /api/health         - Health check")
    print("\nPress Ctrl+C to stop the server")

    app.run(debug=True, host='0.0.0.0', port=5000)
