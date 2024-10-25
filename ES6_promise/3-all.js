import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const promises = [createUser(), uploadPhoto()];

  return Promise.all(promises)
    .then((results) => {
      const [user, photo] = results;
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => console.log('Signup system offline'));
}
