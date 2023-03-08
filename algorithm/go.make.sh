
echo "Enter a filename for your new Markdown file (without the .md extension):"
read filename
echo "Enter url"
read url

cat << EOF > "$filename".md
\`\`\`go
// $filename
// $url


\`\`\`
EOF

mv "$filename.md" go/