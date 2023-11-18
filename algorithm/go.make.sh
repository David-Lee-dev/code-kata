
echo "Enter a filename for your new Markdown file (without the .go extension):"
read filename
echo "Enter url"
read url

cat << EOF > "$filename".go
// $filename
// $url


EOF

mv "$filename.go" go/