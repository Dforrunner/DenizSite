const { watch, series, src, dest } = require('gulp');
const rename = require('gulp-rename');
const uglifycss = require('gulp-uglifycss');
const uglify = require('gulp-uglify-es').default;
const htmlmin = require('gulp-htmlmin');

// Minify CSS
function minifyCSS() {
    return src('./mySite/static/mySite/stylesheets/css/main.css')
    .pipe(uglifycss({
      "uglyComments": true
    }))
    .pipe(rename({extname:'.min.css'}))
    .pipe(dest('./mySite/static/mySite/stylesheets/css/'));
}

// Minify JS
function minifyJS() {
    return src("./mySite/static/mySite/scripts/*.js")
        .pipe(rename({extname:'.min.js'}))
        .pipe(uglify())
        .pipe(dest("./mySite/static/mySite/scripts/minJS"));
}

// Minify HTML
function minifyHTML(){
  return src('./mySite/templates/mySite/*.html')
    .pipe(htmlmin({ collapseWhitespace: true }))
    .pipe(dest('./mySite/templates/mySite/minHTML'));
}

exports.build = series(minifyCSS, minifyJS, minifyHTML);
exports.default = function (){
    watch(
        './mySite/static/mySite/stylesheets/scss/*.scss',
        series(minifyCSS)
    );

    watch(
        './mySite/static/mySite/scripts/*.js',
        series(minifyJS)
    );
     watch(
        './mySite/templates/mySite/*.html',
        series(minifyHTML)
    );
};