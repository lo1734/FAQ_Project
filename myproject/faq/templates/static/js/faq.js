fetch('/api/faqs?lang=en')
  .then(response => response.json())
  .then(data => {
    const faqContainer = document.getElementById('faq-container');
    data.forEach(faq => {
        const faqElement = document.createElement('div');
        faqElement.innerHTML = `<h3>${faq.question}</h3><p>${faq.answer}</p>`;
        faqContainer.appendChild(faqElement);
    });
  });
