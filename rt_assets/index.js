const DAY_OF_MONTH = '25';
const MONTH = 'Jun';
const YEAR = '2023';
const HOUR = '12';
const MINUTES = '30';
const SECONDS = '00';

const PRELOADER_TIME = '500';
// const LIVE_URL = 'https://www.google.com';

const LAUNCH_DATE = `${MONTH} ${DAY_OF_MONTH}, ${YEAR} ${HOUR}:${MINUTES}:${SECONDS}`;

const countDownDate = new Date(LAUNCH_DATE).getTime();
const x = setInterval(() => {
  const now = new Date().getTime();
  const distance = countDownDate - now;

  const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  const hours = Math.floor(
    (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
  );
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);

  document.getElementById('days').innerHTML = days;
  document.getElementById('hours').innerHTML = hours;
  document.getElementById('minutes').innerHTML = minutes;
  document.getElementById('seconds').innerHTML = seconds;

  if (distance < 0) {
    clearInterval(x);
    document.getElementById('days').innerHTML = '00';
    document.getElementById('hours').innerHTML = '00';
    document.getElementById('minutes').innerHTML = '00';
    document.getElementById('seconds').innerHTML = '00';
    // window.open(LIVE_URL, '_self')
  }
}, 1000);

window.addEventListener('load', (event) => {
  setTimeout(() => {
    console.log('Jello');
    const body = document.querySelector('body');
    body.classList.add('loaded');
  }, PRELOADER_TIME);
});
