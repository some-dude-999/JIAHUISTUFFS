/**
 * Luke Hydro CRM - Google Apps Script Backend
 *
 * SETUP INSTRUCTIONS:
 * 1. Open your Google Sheet
 * 2. Click Extensions → Apps Script
 * 3. Delete any existing code
 * 4. Paste this entire script
 * 5. Click Deploy → New Deployment
 * 6. Select "Web app"
 * 7. Execute as: "Me"
 * 8. Who has access: "Anyone"
 * 9. Click Deploy
 * 10. Copy the Web App URL
 * 11. Paste it into the HTML (APPS_SCRIPT_URL variable)
 */

// Sheet configuration
const SHEET_NAME = 'Sheet1'; // Change this to your sheet tab name

function doGet(e) {
  return handleRequest(e);
}

function doPost(e) {
  return handleRequest(e);
}

function handleRequest(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);

    if (!sheet) {
      return ContentService.createTextOutput(JSON.stringify({
        success: false,
        error: 'Sheet not found: ' + SHEET_NAME
      })).setMimeType(ContentService.MimeType.JSON);
    }

    const action = e.parameter.action || 'get';

    if (action === 'get') {
      return getContacts(sheet);
    } else if (action === 'save') {
      return saveContacts(sheet, e);
    }

    return ContentService.createTextOutput(JSON.stringify({
      success: false,
      error: 'Unknown action: ' + action
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      success: false,
      error: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function getContacts(sheet) {
  const data = sheet.getDataRange().getValues();

  if (data.length === 0) {
    return ContentService.createTextOutput(JSON.stringify({
      success: true,
      contacts: []
    })).setMimeType(ContentService.MimeType.JSON);
  }

  const headers = data[0];
  const contacts = [];

  for (let i = 1; i < data.length; i++) {
    const row = data[i];
    const contact = {};

    for (let j = 0; j < headers.length; j++) {
      contact[headers[j]] = row[j] || '';
    }

    contacts.push(contact);
  }

  return ContentService.createTextOutput(JSON.stringify({
    success: true,
    contacts: contacts
  })).setMimeType(ContentService.MimeType.JSON);
}

function saveContacts(sheet, e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const contacts = data.contacts;

    if (!contacts || !Array.isArray(contacts)) {
      throw new Error('Invalid contacts data');
    }

    // Clear existing data (keep headers)
    if (sheet.getLastRow() > 1) {
      sheet.deleteRows(2, sheet.getLastRow() - 1);
    }

    // Set headers
    const headers = ['Date Contacted', 'PIC', 'Business', 'Number', 'Location',
                     'Attempts', 'Notes', 'Probability', 'Email', 'Business Type', 'Starred'];
    sheet.getRange(1, 1, 1, headers.length).setValues([headers]);

    // Add contacts
    if (contacts.length > 0) {
      const rows = contacts.map(c => [
        c.date || '',
        c.pic || '',
        c.business || '',
        c.number || '',
        c.location || '',
        c.attempts || '0',
        c.notes || '',
        c.probability || '',
        c.email || '',
        c.businessType || '',
        c.starred ? 'true' : 'false'
      ]);

      sheet.getRange(2, 1, rows.length, headers.length).setValues(rows);
    }

    return ContentService.createTextOutput(JSON.stringify({
      success: true,
      message: 'Saved ' + contacts.length + ' contacts',
      timestamp: new Date().toISOString()
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      success: false,
      error: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}
