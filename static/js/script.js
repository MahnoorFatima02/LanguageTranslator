function getTranslation() {
    const textInput = document.getElementById('text_input').value;
    document.body.style.cursor = 'wait';
    document.getElementById('loadingSpinner').style.display = 'block';

    fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'translation_text': textInput
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerHTML = 
            `<p>Translated Text: ${data.translated_text}</p>`;
    })
    .catch(error => {
        console.error('Error:', error);
    })
    .finally(() => {
        document.body.style.cursor = 'default';
        document.getElementById('loadingSpinner').style.display = 'none';
    });;
}