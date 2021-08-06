# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:23:04 2020

@author: avsista
"""

import uuid
import logging
import datetime
import hashlib
import json
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
from flask import Flask, jsonify
from uuid import UUID

logging.getLogger().setLevel(logging.INFO)

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)

class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, bidderinfo = "Genesis block", previous_hash = '0')

    def create_block(self, proof, bidderinfo, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'bidderinfo': bidderinfo,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

class TenderInfo:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4, separators=(',', ': '))
    
    def __init__(self):
        self.Title = 'Production of COVAXIN Coivid-19 Vaccine'
        self.Description = 'This tender is to produce 10 Cr doses of Covid-19 vaccine of brand Covaxin by end of 31st March 2021. Quality would be monitored by ICMR'
        self.Tender_StartDate = '16 Sep 2020'
        self.Tender_EndDate = '30 Sep 2020'

class Item:
    def __init__(self, name, reserved_price):
        self.id = uuid.uuid4()
        self.name = name
        self.reserved_price = reserved_price
        self.is_sold = False
        
        
class Participant:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    def __init__(self, name, finalscore):
        self.id = json.dumps(uuid.uuid4(), cls=UUIDEncoder)
        self.name = name
        self.finalscore = finalscore

    def bid(self, auction):
        Bid(self, auction)
        
#     def createCriteria(self, criterion1, criterion2, criterion3):
#         return BidderCriteria(self, criterion1, criterion2, criterion3)


# class BidderCriteria:
#     def __init__(self, bidder, criterion1, criterion2, criterion3):
#         self.bidder = bidder
#         self.criterion1 = criterion1
#         self.criterion2 = criterion2
#         self.criterion3 = criterion3
        
        
class Auction:
    def __init__(self, item):
        if item.is_sold:
            logging.error("Item {} already sold".format(item.name))
        else:
            self.id = uuid.uuid4()
            self.item = item
            self.is_started = False
            self.has_failed = None
            self.highest_bid = None

    # An auction can be started if it has not already failed
    def start(self):
        if self.has_failed is not None:
            logging.error("Auction {} already performed "
                          "on this item.".format(self.id))
        else:
            self.is_started = True
            logging.info("Auction {} has been started".format(self.id))

    # An auction can be stopped if it's started
    # If the reserved price is not met, the auction is tagged as failed
    def stop(self):
        if self.is_started:
            highest_bid = self.highest_bid
            if (highest_bid is None or
                    (highest_bid is not None and
                     self.item.reserved_price > highest_bid.amount)):
                self.has_failed = True
                logging.warning("Auction {} did not reach "
                                "the reserved price".format(self.id))
            else:
                self.has_failed = False
                self.item.is_sold = True
            self.is_started = False
            logging.info("Auction {} has been stopped".format(self.id))
        else:
            logging.error("Auction {} is not started. "
                          "You can't stop it.".format(self.id))
            
        
class Bid:
    def __init__(self, bidder, auction):
        if not auction.is_started:
            logging.warning("Auction {} has not been started yet. "
                            "Bid is not allowed".format(auction.id))
        # elif auction.highest_bid is not None \
        #         and auction.highest_bid.amount >= amount:
        #     logging.error("A new bid has to have a price higher than "
        #                   "the current highest bid.")
        else:
            self.id = uuid.uuid4()
            self.bidder = bidder
            self.auction = auction
            self.auction.highest_bid = self
            logging.info("{} bids for auction {}".format(bidder.name, auction.id))
            
class BidEvaluator:
    def __init__(self, weight1, weight2, weight3, weight4, weight5, weight6, weight7, weight8, weight9):
        self.weight1 = weight1
        self.weight2 = weight2
        self.weight3 = weight3
        self.weight4 = weight4
        self.weight5 = weight5
        self.weight6 = weight6
        self.weight7 = weight7
        self.weight8 = weight8
        self.weight9 = weight9
        
    def EvaluateBid(self, bidder):
        return WeightedCriteria(self, bidder)
        
        
class WeightedCriteria:
    def __init__(self, bidevaluator, bidder):
        self.bidevaluator = bidevaluator
        self.bidder = bidder
        self.weightedCriterion1 = bidevaluator.weight1 * 0.1
        self.weightedCriterion2 = bidevaluator.weight2 * 0.1
        self.weightedCriterion3 = bidevaluator.weight3 * 0.1
        self.weightedCriterion4 = bidevaluator.weight4 * 0.1
        self.weightedCriterion5 = bidevaluator.weight5 * 0.1
        self.weightedCriterion6 = bidevaluator.weight6 * 0.1
        self.weightedCriterion7 = bidevaluator.weight7 * 0.1
        self.weightedCriterion8 = bidevaluator.weight8 * 0.15
        self.weightedCriterion9 = bidevaluator.weight9 * 0.15
      

class AwardContract:
    def __init__(self):
        self.tenderWeights = []
        self.bidders = []
        
    def AddToTender(self, weightedCriteria):
        self.tenderWeights.append(weightedCriteria)
        #self.bidders.append(bidder)
        
    def GetTotalCriteriaForBidder(self, bidder):
        self.weightsArray = []
        self.sumOfWeight1 = 0
        self.sumOfWeight2 = 0
        self.sumOfWeight3 = 0
        self.sumOfWeight4 = 0
        self.sumOfWeight5 = 0
        self.sumOfWeight6 = 0
        self.sumOfWeight7 = 0
        self.sumOfWeight8 = 0
        self.sumOfWeight9 = 0
        
        evalList = list(filter(lambda a: a.bidder.name == bidder.name, self.tenderWeights))
        for x in range(len(evalList)):
            self.sumOfWeight1 += evalList[x].weightedCriterion1
            self.sumOfWeight2 += evalList[x].weightedCriterion2
            self.sumOfWeight3 += evalList[x].weightedCriterion3
            self.sumOfWeight4 += evalList[x].weightedCriterion4
            self.sumOfWeight5 += evalList[x].weightedCriterion5
            self.sumOfWeight6 += evalList[x].weightedCriterion6
            self.sumOfWeight7 += evalList[x].weightedCriterion7
            self.sumOfWeight8 += evalList[x].weightedCriterion8
            self.sumOfWeight9 += evalList[x].weightedCriterion9
            
        weightedAvgOfWeight1 = self.sumOfWeight1/len(evalList)
        weightedAvgOfWeight2 = self.sumOfWeight2/len(evalList)
        weightedAvgOfWeight3 = self.sumOfWeight3/len(evalList)
        weightedAvgOfWeight4 = self.sumOfWeight4/len(evalList)
        weightedAvgOfWeight5 = self.sumOfWeight5/len(evalList)
        weightedAvgOfWeight6 = self.sumOfWeight6/len(evalList)
        weightedAvgOfWeight7 = self.sumOfWeight7/len(evalList)
        weightedAvgOfWeight8 = self.sumOfWeight8/len(evalList)
        weightedAvgOfWeight9 = self.sumOfWeight9/len(evalList)
        
        totalScore = (weightedAvgOfWeight1+weightedAvgOfWeight2+weightedAvgOfWeight3+
                      weightedAvgOfWeight4+weightedAvgOfWeight5+weightedAvgOfWeight6+
                      weightedAvgOfWeight7+weightedAvgOfWeight8+weightedAvgOfWeight9)
        self.weightsArray.extend((weightedAvgOfWeight1, weightedAvgOfWeight2, weightedAvgOfWeight3, 
                                  weightedAvgOfWeight4, weightedAvgOfWeight5, weightedAvgOfWeight6,
                                  weightedAvgOfWeight7, weightedAvgOfWeight8, weightedAvgOfWeight9, 
                                  totalScore))
        return self.weightsArray
                
           
    
class Evaluator:
    def __init__(self):
        self.id = uuid.uuid1()
        self.auctions = []

    def add_auction(self, auction):
        existing_auctions = list(filter(lambda a: a.id == auction.id, self.auctions))
        if existing_auctions:
            logging.error("Auction {} has already been "
                          "added to the evaluation".format(auction.id))
        else:
            self.auctions.append(auction)

    def latest_auction_by_item_name(self, name):
        auction = list(filter(lambda a: a.item.name == name, self.auctions))[0]
        if auction is None:
            status = "The item {} has no auctions".format(name)
        else:
            status = "The latest auction for the item {} is \n".format(name)
            if auction.has_failed:
                status += "Auction for item {} did not " \
                          "reach the reserved price {}" \
                    .format(name, auction.item.reserved_price)
            else:
                if auction.highest_bid is None:
                    status += "No bidder for auction {} of item {}"\
                        .format(auction, name)
                else:
                    if auction.is_started:
                        status += "{} leads the auction with " \
                                  "the amount {}" \
                            .format(auction.highest_bid.bidder.name,
                                    auction.highest_bid.amount)
                    else:
                        status += "{} has been sold to {} " \
                                  "for the amount {}" \
                            .format(name,
                                    auction.highest_bid.bidder.name,
                                    auction.highest_bid.amount)
        return status

app = Flask(__name__)  
@app.route('/get_chain', methods = ['GET'])
def get_chain(): 

# def main():
    blockchain = Blockchain()
    evaluator = Evaluator()

    bidder1 = Participant("HSI Ltd.", 0)
    bidder2 = Participant("PPM Ltd.", 0)
    bidder3 = Participant("GeoSpat Ltd.", 0)

    siteName = "Divya Sree Trinity"
    site = Item(siteName, 1000)
    auctionSite = Auction(site)

    evaluator.add_auction(auctionSite)

    auctionSite.start()

    bidder1.bid(auctionSite)
    bidder2.bid(auctionSite)
    
    bidevaluator1 = BidEvaluator(8, 7, 8, 7, 8, 7, 6, 7, 5)
    bidevaluator2 = BidEvaluator(9, 8, 9, 8, 9, 8, 9, 8, 6)
    
    eval1ForBidder1 = bidevaluator1.EvaluateBid(bidder1)
    eval2ForBidder1 = bidevaluator2.EvaluateBid(bidder1)
    
    bidevaluator1 = BidEvaluator(8, 7, 8, 7, 5, 8, 7, 8, 7)
    bidevaluator2 = BidEvaluator(9, 8, 9, 8, 6, 9, 8, 9, 8)
    
    eval1ForBidder2 = bidevaluator1.EvaluateBid(bidder2)
    eval2ForBidder2 = bidevaluator2.EvaluateBid(bidder2)
    
    bidevaluator1 = BidEvaluator(5, 8, 7, 5, 6, 7, 5, 6, 7)
    bidevaluator2 = BidEvaluator(6, 9, 8, 6, 9, 8, 6, 9, 8)
    
    eval1ForBidder3 = bidevaluator1.EvaluateBid(bidder3)
    eval2ForBidder3 = bidevaluator2.EvaluateBid(bidder3)
    
    awardContract = AwardContract()
    awardContract.AddToTender(eval1ForBidder1)
    awardContract.AddToTender(eval2ForBidder1)
    
    awardContract.AddToTender(eval1ForBidder2)
    awardContract.AddToTender(eval2ForBidder2)
    
    awardContract.AddToTender(eval1ForBidder3)
    awardContract.AddToTender(eval2ForBidder3)
    
    bidder1Score = awardContract.GetTotalCriteriaForBidder(bidder1)
    bidder2Score = awardContract.GetTotalCriteriaForBidder(bidder2)
    bidder3Score = awardContract.GetTotalCriteriaForBidder(bidder3)
    
    bidder1.finalscore = bidder1Score[9]
    bidder2.finalscore = bidder2Score[9]
    bidder3.finalscore = bidder3Score[9]

    data = [[bidder1.name, bidder1Score[9]], 
            [bidder2.name, bidder2Score[9]],
            [bidder3.name, bidder3Score[9]]]
    
    df = pd.DataFrame(data, columns = ['Bidders', 'Total Weighted Average'] ) 
  
    # create histogram for numeric data 
    #df.hist() 
  
    # show plot 
    #plt.show() 
    
    #df.plot.bar() 
  
    # plot between 2 attributes 
    plt.bar(df['Bidders'], df['Total Weighted Average']) 
    plt.xlabel("Bidders", fontweight='bold') 
    plt.ylabel("Total Weighted Average", fontweight='bold') 
    barlist = plt.bar(df['Bidders'], df['Total Weighted Average'])
    barlist[0].set_color('r')
    barlist[1].set_color('g')
    barlist[2].set_color('b')

    plt.ylim(0, max(df['Total Weighted Average'])+1)
    plt.yticks(np.arange(0, max(df['Total Weighted Average']+0.5), 0.5))
    plt.autoscale(enable=True, axis='y', tight=None)
    plt.show() 
    
    # plot based on weighted averages
    barWidth = 0.25
    bars1 = [bidder1Score[0], bidder1Score[1], bidder1Score[2], 
             bidder1Score[3], bidder1Score[4], bidder1Score[5], 
             bidder1Score[6], bidder1Score[7], bidder1Score[8]]
    
    bars2 = [bidder2Score[0], bidder2Score[1], bidder3Score[2], 
             bidder2Score[3], bidder2Score[4], bidder2Score[5], 
             bidder2Score[6], bidder2Score[7], bidder2Score[8]]
    
    bars3 = [bidder3Score[0], bidder3Score[1], bidder3Score[2], 
             bidder3Score[3], bidder3Score[4], bidder3Score[5], 
             bidder3Score[6], bidder3Score[7], bidder3Score[8]]
    
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    
    plt.bar(r1, bars1, color='r', width=barWidth, edgecolor='white', label=bidder1.name)
    plt.bar(r2, bars2, color='g', width=barWidth, edgecolor='white', label=bidder2.name)
    plt.bar(r3, bars3, color='b', width=barWidth, edgecolor='white', label=bidder3.name)
    
    plt.xlabel('Evaluation Criteria', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], 
               ['Relevant Experience', 'Financial Capital', 'Appreciations', 
                'Past Performance', 'Methodology', 'Operational Data', 
                'Resources', 'Scope of work', 'Price'], rotation=90)
    plt.autoscale(enable=True, axis='both', tight=True)
    
    plt.ylabel('Weighted Average', fontweight='bold')
    plt.xlim(-0.5, 9)
    plt.ylim(0, max(max(bars1), max(bars2), max(bars3))+0.2)

    plt.legend()
    plt.show()
    
    # Add Bidder1 to blockchain       
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.create_block(proof, bidder1.toJSON(), previous_hash)
    
    # Add Bidder 2 to blockchain
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.create_block(proof, bidder2.toJSON(), previous_hash)
    
    # Add Bidder 3 to blockchain
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.create_block(proof, bidder3.toJSON(), previous_hash)
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

app.run(host = '0.0.0.0', port = 5000) 

# if __name__ == '__main__':
#     main()

          