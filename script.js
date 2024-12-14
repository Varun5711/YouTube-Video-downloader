function downloadVideo() {
            const url = document.getElementById('url').value;
            fetch('http://localhost:8000/download', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ url: url })
            })
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        alert('An error occurred: ' + data.error);
                    } else {
                        alert('Download successful! Filename: ' + data.filename);
                    }
                })
                .catch(error => {
                    alert('An unexpected error occurred: ' + error);
                });
        }
