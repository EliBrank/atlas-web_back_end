import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [signUpUser(firstName, lastName), uploadPhoto(fileName)];

  return Promise.allSettled(promises)
    .then((results) => results.map((result) => ({
      status: result.status,
      // assign value or error to key depending on status
      value: result.status === 'fulfilled' ? result.value : `Error: ${result.reason.message}`,
    })));
}
