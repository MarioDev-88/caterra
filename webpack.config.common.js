const path = require("path");

const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  //   mode: "development",
  //   context: path.resolve(__dirname, "assets"),
  entry: {
    bundle: path.resolve(__dirname, "src", "static", "js", "main.js"),
  },
  output: {
    filename: "bundle.dist.js",
    path: path.resolve(__dirname, "src", "static", "js"),
  },
  plugins: [new MiniCssExtractPlugin({ filename: "../css/[name].dist.css" })],
  module: {
    rules: [
      {
        test: /\.(css|scss)$/,
        exclude: /node_modules/,
        use: [
          // "style-loader",
          MiniCssExtractPlugin.loader,
          {
            loader: "css-loader",
            options: {
              importLoaders: 1,
              url: false,
            },
          },
          {
            loader: "postcss-loader",
            options: {
              postcssOptions: {
                ident: "postcss",
                plugins: [require("tailwindcss"), require("autoprefixer")],
              },
            },
          },
          "sass-loader",
        ],
      },
    ],
  },
};
