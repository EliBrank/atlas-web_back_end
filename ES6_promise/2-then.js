export default async function handleResponseFromAPI(promise) {
  try {
    const success = await promise;
    return {
      status: 200,
      data: success,
    };
  } catch (error) {
    return {
      success: false,
      error: {},
    };
  } finally {
    console.log('Got a response from the API');
  }
}
