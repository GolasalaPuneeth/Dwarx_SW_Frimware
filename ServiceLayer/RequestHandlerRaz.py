from .IRequestHandlerRaz import IcustomerRequest
import asyncio

class CustomerRequest(IcustomerRequest):
    async def forward_to_esp(self, qrid, amount, vpa):
        print(qrid,amount,vpa)
        return True # super().forword_to_esp(qrid, amount, vpa)
    
async def main():
    tst = IcustomerRequest()
    result = await tst.forward_to_esp("hdbf", "zfz", "sdfs")
    print(f"Result: {result}")

# Run the test
if __name__ == "__main__":
    asyncio.run(main())
