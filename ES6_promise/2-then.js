export default async function handleResponseFromAPI(promise) {
  try {
    const success = await promise;
    return {
      status: 200,
      body: success,
    };
  } catch (error) {
    return {
      error: {},
    };
  } finally {
    console.log('Got a response from the API');
  }
}
