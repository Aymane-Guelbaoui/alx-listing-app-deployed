import ListingCard from '../components/ListingCard'
import { listings } from './api/listings'

export default function Home() {
  return (
    <div>
      <h1>Listings</h1>
      {listings.map(listing => <ListingCard key={listing.id} listing={listing} />)}
    </div>
  )
}
