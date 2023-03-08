
echo "Enter a filename for your new Markdown file (without the .py extension):"
read filename
echo "Enter url"
read url

cat << EOF > "$filename".py
\`\`\`python3
// $filename
// $url


\`\`\`
EOF

mv "$filename.py" python/