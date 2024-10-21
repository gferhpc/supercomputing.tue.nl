usage () {
	echo "Usage: $0 -N max_iterations [ -n sub_iterations ] -c checkpoint_file"
	exit 1
}

sub_iterations=-1

while getopts "N:n:c:" arg; do
	case "$arg" in
	N) max_iterations="$OPTARG" ;;
	n) sub_iterations="$OPTARG" ;;
	c) checkpoint_file="$OPTARG" ;;
	*) usage ;;
	esac
done

if [ -z "$max_iterations" -o -z "$checkpoint_file" ]; then
	usage
fi

checkpoint_file_new=$checkpoint_file.new

echo "Attempting to read checkpoint from $checkpoint_file..."
if [ -f $checkpoint_file ]; then
	read iteration_counter < $checkpoint_file
	echo "Checkpoint file read; iteration counter is $iteration_counter."
else
	iteration_counter=0
	echo "Checkpoint file couldn't be read; iteration counter is 0."
fi

while true; do

	if [ $iteration_counter -ge $max_iterations ]; then
		echo "Reached max total iterations (=$max_iterations). Stopping."
		break
	fi

	if [ $sub_iterations -eq 0 ]; then
		echo "Reached max iterations for subjob. Stopping."
		break
	fi
	sub_iterations=$((sub_iterations-1))

	iteration_counter=$((iteration_counter+1))
	echo "Doing iteration $iteration_counter..."
	sleep 25
	echo "Finished iteration $iteration_counter."

	echo $iteration_counter > $checkpoint_file_new
	mv $checkpoint_file_new $checkpoint_file
	echo "Stored checkpoint to $checkpoint_file."

done
