function deleteStory(storyId) {
    fetch('/delete-story', {
        method: 'POST',
        body: JSON.stringify({ storyId: storyId }),
}).then((_res) => {
    window.location.href = '/';
})
}


