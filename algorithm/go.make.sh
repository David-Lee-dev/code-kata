
echo "Enter a filename for your new Markdown file (without the .go extension):"
read filename
echo "Enter url"
read url

allowed_sources=("programmers" "swea" "beakjoon")
echo "Select a source (options: ${allowed_sources[*]}):"
select source in "${allowed_sources[@]}"; do
  if [[ " ${allowed_sources[*]} " == *" $source "* ]]; then
    break
  else
    echo "Invalid source. Please select a valid source."
  fi
done

if [ "$source" == "swea" ]; then
  destination="go/$source/$filename"
  mkdir -p "$destination"
else
  destination="go/$source"
fi

cat << EOF > "$destination/$filename.go"
// $filename
// $url


EOF