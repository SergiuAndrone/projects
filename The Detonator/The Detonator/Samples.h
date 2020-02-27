//
//  Samples.h
//  The Detonator
//
//  Created by sergiuandrone on 28/11/2019.
//  Copyright © 2019 sergiuandrone. All rights reserved.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface Samples : NSObject

+(void)createDefaulLocation;
+(NSNumber*)currentTimestamp;
+(void)runSystemCommand:(NSString*)cmd;
+(void)dropBatTrojan:(NSString*)destination;
+(void)dropDialer:(NSString*)destination;
+(void)dropCleanable:(NSString*)destination;
+(void)dropEicar:(NSString*)destination;
+(void)dropKeylogger:(NSString*)destination;
+(void)dropSpyware:(NSString*)destination;
+(void)dropSmartdb:(NSString*)destination;
+(void)dropPacked:(NSString*)destination;
+(void)dropPUA:(NSString*)destination;
+(void)dropAdware:(NSString*)destination;
+(void)dropApplication:(NSString*)destination;
+(void)dropSuspected:(NSString*)destination;
+(void)dropSignedSuspected:(NSString*)destination;
+(void)dropSignedInfected:(NSString*)destination;
+(void)dropMalwareEDR:(NSString*)destination;
+(void)executeRCAPocEdr:(NSString*)destination;
+(void)executePocHttpEdr:(NSString*)destination;
+(void)executeSudospawnATC:(NSString*)destination;

@end

NS_ASSUME_NONNULL_END
