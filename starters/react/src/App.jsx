// The brand's files are in public/brand/; BASE_URL keeps them reachable
// under any path.
const brand = `${import.meta.env.BASE_URL}brand`;
const cards = [
  { for: "Colours", name: "tokens.css", note: "--rs-* variables follow light and dark." },
  { for: "Logo, icons", name: "brand/", note: "All rights reserved: our own pages only." },
  { for: "Deploy", name: "GitHub Pages", note: "A push to master publishes the site." },
];

export default function App() {
  return (
    <main>
      <img className="brand" src={`${brand}/images/logo/mark.svg`} alt="RedScope Technologies" />
      <h1>RedScope Technologies</h1>
      <p className="muted">A React starter in the RedScope style. Replace this page with your own.</p>
      <h2>What is here</h2>
      <div className="grid">
        {cards.map((card) => (
          <div key={card.for} className="card">
            <div className="for">{card.for}</div>
            <div className="name">{card.name}</div>
            <div className="note">{card.note}</div>
          </div>
        ))}
      </div>
      <footer className="muted">© RedScope Technologies</footer>
    </main>
  );
}
