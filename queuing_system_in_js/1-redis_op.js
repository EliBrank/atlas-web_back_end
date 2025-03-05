import redis from "redis";

const client = redis.createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value, callback) {
  client.set(schoolName, value, (err, reply) => {
    redis.print(err, reply);
  });

  if (callback) callback();
}

function displaySchoolValue(schoolName) {
  const schoolValue = client.get(schoolName, (err, reply) => {
    if (err) {
      throw Error(err);
    }
    console.log(reply);
  });
}

client.on('connect', () => {
  console.log('Redis client connected to the server');

  displaySchoolValue('Holberton');

  const newSchool = 'HolbertonSanFrancisco';
  setNewSchool(newSchool, '100', () => {
    displaySchoolValue(newSchool);
  });
});
