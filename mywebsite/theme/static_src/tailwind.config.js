module.exports = {
    content: [
        '../templates/**/*.html', // Templates within theme app (<tailwind_app_name>/templates), e.g. base.html.
        '../../templates/**/*.html', // Main templates directory of the project (BASE_DIR/templates).
        '../../**/templates/**/*.html', // Templates in other Django apps (BASE_DIR/<any_app_name>/templates).
        '../../theme/**/*.js', // All JavaScript files in theme app.
        '../../**/*.py', // All Python files in the project.
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
