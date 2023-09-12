
echo "Enter a filename for your new Markdown file (without the .py extension):"
read filename
echo "Enter url"
read url

allowed_sources=("programmers" "swea")
echo "Select a source (options: ${allowed_sources[*]}):"
select source in "${allowed_sources[@]}"; do
  if [[ " ${allowed_sources[*]} " == *" $source "* ]]; then
    break
  else
    echo "Invalid source. Please select a valid source."
  fi
done

cat << EOF > "$filename".py
# $filename
# $url
# $source

EOF

destination="python/$source/$filename"
mkdir -p "$destination"
mv "$filename.py" "$destination/$filename.py"
