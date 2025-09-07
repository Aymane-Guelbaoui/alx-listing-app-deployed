export const listings = [
  { id: 1, title: 'Beach House', price: 120 },
  { id: 2, title: 'Mountain Cabin', price: 90 }
]

export default function handler(req, res) {
  res.status(200).json(listings)
}
