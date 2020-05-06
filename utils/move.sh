mkdir Hip-Hop
mkdir Pop
mkdir Rock
mkdir Experimental
mkdir Folk
mkdir Jazz
mkdir Electronic
mkdir Spoken
mkdir International
mkdir Soul-RnB
mkdir Blues
mkdir Country
mkdir Classical
mkdir Old-Time-Historic
mkdir Instrumental
mkdir Easy-Listening

while IFS= read -r line
do
  line=( $line )
  dir=$(find . -name "${line[0]}.mp3" | awk -F'[/=]' '{ print $3 }')
  
  if [ ! -z "$dir" ]
  then
        echo "${line[0]} $dir ${line[1]}"
        cp "fma_small/$dir/${line[0]}.mp3" ${line[1]}
  fi
  
done < data.txt
