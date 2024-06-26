

let countdownElement = document.getElementById('countdown');
        let countdown = 5;
        setInterval(function() {
            if (countdown > 1) {
                countdown -= 1;
                countdownElement.textContent = countdown;
            }
        }, 1000);