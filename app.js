
let lotion = require('lotion')
//initial state
let app = lotion({
	initialState: {
		count: 0
	}
})
//transaction handler
app.use(function(state, tx) {
	if (state.count === tx.nonce) {
		state.count++
	}
})

app.start().then(function(appInfo) {
	console.log(`app started. gci: ${appInfo.GCI}`)
})
//npx lotion-cli send 3246d4bf3a1da630e045c7adf372e09cc32cf4428ebcdc44cfbe4d50a5101aad '{ "nonce" : 0 }'
//
