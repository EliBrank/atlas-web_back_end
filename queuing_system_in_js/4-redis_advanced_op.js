import redis from "redis";

const client = redis.createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

async function setNewSchool(schoolName, value) {
  try {
    const setOutput = await setAsync(schoolName, value);
    console.log(`Reply: ${setOutput}`);
  } catch (err) {
    console.error(err);
  }
}

async function displaySchoolValue(schoolName) {
  try {
    const schoolValue = await getAsync(schoolName);
    console.log(schoolValue);
  } catch (err) {
    console.error(err);
  }
}

displaySchoolValue('Holberton');

const newSchool = 'HolbertonSanFrancisco';
setNewSchool(newSchool, '100');
displaySchoolValue(newSchool);
