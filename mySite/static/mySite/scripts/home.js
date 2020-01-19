document.addEventListener('DOMContentLoaded', () => {
	// Making sure we're on the home page before executing scripts
	if(document.querySelector('main').classList.contains('homePage')) {
		// Helper Function that checked if element is in view
		function isInViewport(elem) {
			let bounding = elem.getBoundingClientRect();
			return (
				bounding.top >= 0 &&
				bounding.left >= 0 &&
				bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
				bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
			);
		}

		// Animating section content when they are in view
		const sec2 = document.querySelector('#section2');
		const sec3 = document.querySelector('.sec3-text');
		const sec5 = document.querySelector('.sec5-text');
		const sec6 = document.querySelector('#section6');
		window.addEventListener('scroll', function (event) {
			if (isInViewport(sec2)) {
				document.querySelector('.section2-img-left').classList.add('animated', 'pulse');
				document.querySelector('.section2-img-right').classList.add('animated', 'pulse');
			}
			if (isInViewport(sec3)) {
				document.querySelector('.sec3-content').classList.remove('opacity-0');
				document.querySelector('.sec3-msg-line1').classList.add('animated', 'fadeInLeft');
				document.querySelector('.sec3-msg-line2').classList.add('animated', 'fadeInRight');
				document.querySelector('.sec3-divider').classList.add('animated', 'zoomIn');
			}
			if (isInViewport(sec5)) {
				document.querySelector('.sec5-content').classList.remove('opacity-0');
				document.querySelector('.sec5-msg-line1').classList.add('animated', 'fadeInLeft');
				document.querySelector('.sec5-msg-line2').classList.add('animated', 'fadeInRight');
				document.querySelector('.sec5-divider').classList.add('animated', 'zoomIn');
			}
			if (isInViewport(sec6)) {
				sec6.classList.add('box-wipe-enter-active');
			}
		}, false);
	}
});