// 6-final-user.js

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  try {
    // Use Promise.all to await both promises
    const [userResult, photoResult] = await Promise.all([
      signUpUser(firstName, lastName),
      uploadPhoto(fileName),
    ]);

    // Return an array with the status and value or error of each promise
    return [
      { status: 'fulfilled', value: userResult },
      { status: 'fulfilled', value: photoResult },
    ];
  } catch (error) {
    // If there's an error in any of the promises, return an array with the status and error
    return [
      { status: 'rejected', reason: error.message },
      { status: 'rejected', reason: 'An error occurred in one of the promises.' },
    ];
  }
}

export default handleProfileSignup;
