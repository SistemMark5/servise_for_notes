document.getElementById("postForm").addEventListener("submit", async e => {
  e.preventDefault(); // отменяем стандартную отправку

  const title = document.getElementById("title").value;
  const text = document.getElementById("text").value;

  const res = await fetch("/create_note", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, text, user_id })
  });
  const data = await res.json();
  console.log(data);
});

