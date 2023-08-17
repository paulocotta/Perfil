function TesteSX(){
	for i in {1..5}; do {
		TMP=$(curl --retry 10 --retry-delay 3 --max-time 10 --fail --insecure --silent --location --compressed \
			--output '/dev/null' \
			--write-out '%{http_code}' \
			--request POST 'https://aaaaaaaa/bbbbbbb' \
			--header 'Content-Type: application/json' \
			--data '{"zap_seu": "11946034552"}');
		echo "${TMP}";
		[ "${TMP}" == '200' ] && { break; } || { sleep 5; }
	} done
}

TesteSX;
exit;


function TesteSX(){
	TMP=$(curl \
		--output '/dev/null' \
		--write-out '%{http_code}' \
		--retry 10 \
		--retry-delay 3 \
		--fail \
		--insecure \
		--silent \
		--location \
		--compressed \
		--max-time 10 \
		--request POST 'https://aaaaaaaa/bbbbbbb' \
		--header 'Content-Type: application/json' \
		--data '{"zap_seu": "11946034552"}');
	echo "${TMP}";
	[ "${TMP}" != '201' ] && { TesteSX; }
}

TesteSX;
