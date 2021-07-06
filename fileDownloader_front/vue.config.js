module.exports = {
    devServer: {
        proxy: 'http://localhost:5000/',
        compress: true,
        disableHostCheck: true,
        https: true
    }
}