const riddle = document.querySelector('#js-riddle');
if (riddle) {
	const input = document.querySelector('input');
	const log = document.getElementById('values');
	const encodedStr1 = 'S1BNR3tlQHN5X2J1dF9zdA==';
	const encodedStr2 = 'TExfdHIwdWJsM3NfcHBsfQ==';
	function Random(seed) {
		value = seed * 503 % 701;
		return value;
	}
	input.addEventListener('input', updateValue);
	function updateValue(e) {
		var str = e.target.value;
		if (str == atob(encodedStr1).concat(Random(570).toString(), atob(encodedStr2))) {
			log.textContent = 'Flag correct!';
		} else {
			log.textContent = 'Flag incorrect!';
		}
	}
}

