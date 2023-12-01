import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photoResponse, userResponse]) => {
      console.log(`${photoResponse.body} ${userResponse.firstName} ${userResponse.lastName}`);
      return { photo: photoResponse, user: userResponse };
    })
    .catch((error) => {
      console.error('Signup system offline');
      throw error; // Re-throw the original error for better error handling
    });
}

export default handleProfileSignup;
