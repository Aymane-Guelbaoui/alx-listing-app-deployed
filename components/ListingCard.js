export default function ListingCard({ listing }) {
  return (
    <div>
      <h2>{listing.title}</h2>
      <p>Price: ${listing.price}</p>
    </div>
  )
}
