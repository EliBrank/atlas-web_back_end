const fs = require('fs');
const { parse } = require('csv-parse/sync');

function countStudents(path) {
  try {
    const fileContent = fs.readFileSync(path, 'utf8');

    const records = parse(fileContent, {
      columns: true,
      skip_empty_lines: true,
    });

    console.log(`Number of students: ${records.length}`);
    const fields = new Map();

    for (const record of records) {
      const { field, firstname } = record;

      // check each field to see if already in fields map
      if (!fields.has(field)) {
        // if not, add field with empty array to add student names
        fields.set(field, []);
      }

      fields.get(field).push(firstname);
    }

    // Example output for fields:
    // CS: [Johann, Arielle, Jonathan],
    // SWE: [Guillaume, Joseph, Paul, Tommy]
    for (const [field, students] of fields.entries()) {
      console.log(`Number of students in ${field}: `
                + `${students.length}. List: ${students.join(', ')}`);
    }
  } catch (e) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
