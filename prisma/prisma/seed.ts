import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

async function main() {
  const user = await prisma.user.create({
    data: {
        name:'Bob',
        email: 'bob2@prisma.io',
        transactions:{
            create:{
                amount: 10.00,
                category: "seeding",
                description: "example description",
            }
        },
    },
  })
  console.log(user)
}

main()
  .then(async () => {
    await prisma.$disconnect()
  })
  .catch(async (e) => {
    console.error(e)
    await prisma.$disconnect()
    process.exit(1)
  })