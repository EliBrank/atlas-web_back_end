process.stdin.setEncoding('utf8');

process.stdout.write('Welcome to Holberton School, what is your name? ');

process.stdin.on('readable', () => {
  const chunk = process.stdin.read();
  if (chunk !== null) {
    const name = chunk.trim();
    process.stdout.write(`Your name is: ${name}\n`);
    process.stdin.emit('end');
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
