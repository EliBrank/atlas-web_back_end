import { promises as fs } from 'fs';
import { parse } from 'csv-parse';

export default async function countStudents(path) {
  try {
    const fileContent = await fs.readFile(path, 'utf8');

    const records = await new Promise((resolve, reject) => {
      parse(fileContent, {
        columns: true,
        skip_empty_lines: true,
      }, (err, output) => {
        if (err) {
          reject(err);
        } else {
          resolve(output);
        }
      });
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
