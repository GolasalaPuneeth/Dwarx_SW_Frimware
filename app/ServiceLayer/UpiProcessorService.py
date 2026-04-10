from .IUpiProcessorService import IcustomerRequest
from AppUtils import trigger_esp
# import asyncio

sample_data = {
    1.0 : 1.0,
    5.0 : 5.0,
    10.0: 20.0
}

class CustomerRequest(IcustomerRequest):
    async def push_service(self, qrid, amount, vpa):
        # print(qrid,amount,vpa)
        amount = amount / 100
        if amount in sample_data:
            topik : str = f"payment/{qrid[3:]}/success"
            print(topik)
            await trigger_esp(Customer=vpa,Liters=sample_data[amount],Topic=topik)
            return True
        else:
            print("Not Match Amount")
        return False
    
# async def main():
#     tst = IcustomerRequest()
#     result = await tst.push_service("hdbf", "zfz", "sdfs")
#     print(f"Result: {result}")

# # Run the test
# if __name__ == "__main__":
#     asyncio.run(main())
