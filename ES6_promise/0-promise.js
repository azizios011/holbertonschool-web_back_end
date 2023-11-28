function getResponseFromAPI() {
    return new Promise((resolve) => {
      // Simulate an asynchronous operation (e.g., API call) with setTimeout
      setTimeout(() => {
        resolve("Successful response from the API");
      }, 300); // Simulating a delay of 300 milliseconds
    });
  }
  
  export default getResponseFromAPI;
  