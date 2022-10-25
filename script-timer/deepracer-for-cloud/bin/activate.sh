function dr-update {
    echo "dr-update"
}

function dr-upload-custom-files {
    echo "dr-upload-custom-files"
}

function dr-start-training {
    for i in {1..10}
    do
        echo "Training> Name=main_level/agent, Worker=0, Episode="
        sleep 1
        ((i++))
    done
}

function dr-stop-training {
    echo "dr-stop-training"
}

function dr-start-evaluation {
    echo "\x1b[1mdone\x1b[0m"
}

function dr-stop-evaluation {
    echo "dr-stop-evaluation"
}

echo ran entire file