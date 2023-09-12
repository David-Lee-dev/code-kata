
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

if [ "$source" == "swea" ]; then
  destination="python/$source/$filename"
  mkdir -p "$destination"
else
  destination="python/$source"
fi

cat << EOF > "$destination/$filename.py"
echo "File created at $destination/$filename.py"
